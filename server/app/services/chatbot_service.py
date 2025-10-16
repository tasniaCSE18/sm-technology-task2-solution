import re
from typing import Dict, List
from app.services.product_service import product_service
from app.utils.groq_client import groq_client

class ChatbotService:
    
    async def process_message(self, message: str) -> str:
        
        message_lower = message.lower()
        
        
        if "rating" in message_lower and "above" in message_lower:
            rating_match = re.search(r'(\d+\.?\d*)', message)
            if rating_match:
                min_rating = float(rating_match.group(1))
                products = await product_service.filter_by_rating(min_rating)
                return await self._generate_product_list_response(products, f"products with ratings above {min_rating}")
        
        
        if "electronics" in message_lower or "category" in message_lower:
            category = self._extract_category(message_lower)
            if category:
                products = await product_service.filter_by_category(category)
                return await self._generate_product_list_response(products, f"{category} products")
        
        
        product_name = self._extract_product_name(message)
        if product_name:
            product = await product_service.search_product(product_name)
            if product:
                return await self._generate_product_response(product, message)
        
        
        await product_service.fetch_all_products()
        return await self._generate_general_response(message)
    
    def _extract_product_name(self, message: str) -> str:
       
        keywords = ["about", "price of", "tell me", "show me", "reviews for", "details"]
        for keyword in keywords:
            if keyword in message.lower():
                parts = message.lower().split(keyword)
                if len(parts) > 1:
                    return parts[1].strip().strip("?.,!").split()[0]
        
        
        words = message.lower().split()
        for word in words:
            if len(word) > 3 and word not in ["what", "tell", "show", "about", "price", "more"]:
                return word
        return ""
    
    def _extract_category(self, message: str) -> str:
    
        categories = ["electronics", "furniture", "beauty", "groceries", "fragrances"]
        for cat in categories:
            if cat in message:
                return cat
        return ""
    
    async def _generate_product_response(self, product: Dict, original_message: str) -> str:
     
        product_info = f"""
Product Details:
- Name: {product.get('title')}
- Description: {product.get('description', 'N/A')}
- Price: ${product.get('price')}
- Rating: {product.get('rating', 'N/A')} stars
- Brand: {product.get('brand', 'N/A')}
- Category: {product.get('category', 'N/A')}
- In Stock: {product.get('stock', 0)} units

Customer Question: {original_message}

Generate a natural, friendly response about this product.
"""
        return groq_client.generate_response(product_info)
    
    async def _generate_product_list_response(self, products: List[Dict], query_type: str) -> str:
       
        if not products:
            return f"Sorry, I couldn't find any {query_type}."
        
        product_summary = f"Found {len(products)} {query_type}:\n\n"
        for product in products[:5]:  # Limit to 5 products
            product_summary += f"- {product.get('title')}: ${product.get('price')} (Rating: {product.get('rating', 'N/A')})\n"
        
        if len(products) > 5:
            product_summary += f"\n... and {len(products) - 5} more!"
        
        prompt = f"""
The customer asked about {query_type}.
Here's what we found:
{product_summary}

Generate a helpful, natural response.
"""
        return groq_client.generate_response(prompt)
    
    async def _generate_general_response(self, message: str) -> str:
   
        prompt = f"""
Customer message: {message}

You are an e-commerce assistant. We have various products available including electronics, furniture, beauty products, and more. 
Provide a helpful response to the customer's query.
"""
        return groq_client.generate_response(prompt)

chatbot_service = ChatbotService()