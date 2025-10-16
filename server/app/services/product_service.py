import httpx
from typing import List, Dict, Optional
from app.core.config import settings

class ProductService:
    def __init__(self):
        self.base_url = settings.DUMMYJSON_BASE_URL
        self.products_cache = []
    
    async def fetch_all_products(self) -> List[Dict]:
       
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/products?limit=100")
                response.raise_for_status()
                data = response.json()
                self.products_cache = data.get("products", [])
                return self.products_cache
        except Exception as e:
            return []
    
    async def search_product(self, query: str) -> Optional[Dict]:
       
        if not self.products_cache:
            await self.fetch_all_products()
        
        query_lower = query.lower()
        for product in self.products_cache:
            if query_lower in product.get("title", "").lower():
                return product
        return None
    
    async def filter_by_category(self, category: str) -> List[Dict]:
       
        if not self.products_cache:
            await self.fetch_all_products()
        
        category_lower = category.lower()
        return [p for p in self.products_cache 
                if category_lower in p.get("category", "").lower()]
    
    async def filter_by_rating(self, min_rating: float) -> List[Dict]:
       
        if not self.products_cache:
            await self.fetch_all_products()
        
        return [p for p in self.products_cache 
                if p.get("rating", 0) >= min_rating]

product_service = ProductService()