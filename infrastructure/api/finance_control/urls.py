from django.urls import path

from finance_control.views.login_view import LoginView
from finance_control.views.user_view import UsersView, UserCreateView
from finance_control.views.categories_view import CategoriesView
from finance_control.views.cards_view import CardsView
from infrastructure.api.finance_control.views.accounts_view import AccountView
from finance_control.views.subcategories_view import SubcategoryView, SubcategoryByCategory
from finance_control.views.goals_view import GoalView, GoalByCategoryView
from finance_control.views.transactions_view import TransactionView, TransactionViewByCategory, TransactionViewBySubategory

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('users/', UsersView.as_view(), name='users-list'),
    path('users/<uuid:pk>/', UsersView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='users-list'),
    path('categories/', CategoriesView.as_view(), name='categories-list'),
    path('categories/<uuid:pk>/', CategoriesView.as_view(), name='category-detail'),
    path('cards/', CardsView.as_view(), name='cards-list'),
    path('cards/<uuid:pk>/', CardsView.as_view(), name='card-detail'),
    path('accounts/', AccountView.as_view(), name='accounts-list'),
    path('accounts/<uuid:pk>/', AccountView.as_view(), name='account-detail'),
    path('subcategories/<uuid:pk>/', SubcategoryView.as_view(), name='subcategory-detail'),
    path('subcategories/', SubcategoryView.as_view(), name='subcategories-list'),
    path('subcategories/category/<uuid:pk>/', SubcategoryByCategory.as_view(), name='subcategories-by-category'),
    path('goals/', GoalView.as_view(), name='goals-list'),
    path('goals/<uuid:pk>/', GoalView.as_view(), name='goal-detail'),
    path('goals/category/<uuid:pk>/', GoalByCategoryView.as_view(), name='goals-by-category'),
    path('transactions/', TransactionView.as_view(), name='transaction-detail'),
    path('transactions/<uuid:pk>', TransactionView.as_view(), name='transaction-list'),
    path('transactions/category/<uuid:pk>', TransactionViewByCategory.as_view(), name='transaction-by-category'),
    path('transactions/subcategories/<uuid:pk>', TransactionViewBySubategory.as_view(), name='transaction-by-subcategories'),
]
