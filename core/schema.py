import graphene
from graphene_django import DjangoObjectType

from core.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    ingredient_by_name = graphene.Field(IngredientType, name=graphene.String(required=True))
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.all()
    
    def resolve_ingredient_by_name(root, info, name): 
        return Ingredient.objects.get(name=name)

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
    

schema = graphene.Schema(query=Query)