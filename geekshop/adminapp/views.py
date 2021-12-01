from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from adminapp.forms import ShopUserAdminEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, reverse
from adminapp.forms import ProductCategoryEditForm
from mainapp.models import Product, ProductsCategory
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'
    login_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'
        return context

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context)

class UserCreateView(LoginRequiredMixin, CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')

# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES )
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'user_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)

class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')

# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk )
#
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     context = {
#         'title': title,
#         'edit_form': edit_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#
#     context = {
#         'title': title,
#         'user_to_delete': user
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)

class CategoryListView(LoginRequiredMixin, ListView):
    model = ProductsCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'
    login_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'админка/категории'
        return context

# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductsCategory.objects.all()
#
#     context = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', context)

class CategoryCreateView(CreateView):
    model = ProductsCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context['title'] = 'категория/создание'
        return context

# def category_create(request):
#     title = 'категория/создание'
#
#     if request.method == 'POST':
#         category_form = CategoryCreationForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#     else:
#         category_form = CategoryCreationForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form
#     }
#
#     return render(request, 'adminapp/category_create.html', context)

class CategoryUpdateView(UpdateView):
    model = ProductsCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data()
        context['title'] = 'категория/редактирование'
        return context

# def category_update(request, pk):
#     title = 'категория/редактирование'
#     edit_category = get_object_or_404(ProductsCategory, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = CategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = CategoryEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'category_form': edit_form,
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class CategoryDeleteView(DeleteView):
    model = ProductsCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data()
        context['title'] = 'категория/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# def category_delete(request, pk):
#     title = 'категория/удаление'
#
#     category = get_object_or_404(ProductsCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#
#     context = {
#         'title': title,
#         'category_to_delete': category
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)

class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    context_object_name = 'objects'
    login_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'админка/продукты'
        context['category'] = get_object_or_404(ProductsCategory, pk=self.kwargs['pk'])
        context['products_list'] = self.object_list.filter(category__pk=self.kwargs['pk']).order_by('name')
        return context

# def products(request, pk):
#     title = 'админка/продукт'
#     category = get_object_or_404(ProductsCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', context)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data()
        context['title'] = 'продукт/создание'
        context['category'] = get_object_or_404(ProductsCategory, pk=self.kwargs['pk'])
        return context

    def get_initial(self):
        category = get_object_or_404(ProductsCategory, pk=self.kwargs['pk'])
        return {'category': category}

    def get_success_url(self):
        return reverse_lazy('admin_staff:products', args=[self.object.category_id])



# def product_create(request, pk):
#     title = 'продукт/создание'
#     category = get_object_or_404(ProductsCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     context = {
#         'title': title,
#         'product_form': product_form,
#         'category':category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)

class ProductReadView(ListView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        object = get_object_or_404(Product, pk=self.kwargs['pk'])
        context = super(ProductReadView, self).get_context_data()
        context['title'] = 'продукт/детали'
        context['object'] = object
        context['category'] = get_object_or_404(ProductsCategory, pk=object.category_id)
        return context

    def get_success_url(self):
        object = get_object_or_404(Product, pk=self.kwargs['pk'])
        category_id = object.category_id
        return reverse_lazy('admin_staff:products', args=[category_id])

# def product_read(request, pk):
#     title = 'продукт/подробнее'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'title': title,
#         'object': product,
#     }
#
#     return render(request, 'adminapp/product_read.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data()
        context['title'] = 'продукт/редактирование'
        return context

    def get_success_url(self):
        return reverse_lazy('admin_staff:products', args=[self.object.category_id])


# def product_update(request, pk):
#     title = 'продукт/редактирование'
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     context = {
#         'title': title,
#         'product_form': edit_form,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_staff:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data()
        context['title'] = 'продукт/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#     category_id = product.category
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': product,
#         # 'category_id': category_id,
#     }
#
#     return render(request, 'adminapp/product_delete.html', context)
