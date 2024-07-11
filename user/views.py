from rest_framework.viewsets import ModelViewSet


class UserModelViewSet(ModelViewSet):
    pass # todo



# import json
# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
# from .forms import CustomerUserCreationForm, CustomerUserChangeForm
# from .models import User
#
#
# @ensure_csrf_cookie
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all().values()
#         return JsonResponse(list(users), safe=False)
#
#
# @csrf_exempt
# def user_create(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         form = CustomerUserCreationForm(data)
#         if form.is_valid():
#             user = form.save()
#             return JsonResponse({'id': user.id, 'username': user.username})
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({'errors': errors}, status=400)
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)
#
#
#
# @csrf_exempt
# def user_edit(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         form = CustomerUserChangeForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save()
#             return JsonResponse({'id': user.id, 'name': user.name})
#     return JsonResponse({'error': 'Invalid form data'}, status=400)
#
#
# @csrf_exempt
# def user_delete(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         user.delete()
#         return JsonResponse({'id': pk})
#     return JsonResponse({'error': 'Invalid request'}, status=400)
#
#
# # 使用 django 內建渲染寫法
# # from django.shortcuts import render, redirect, get_object_or_404
# # from .forms import UserCreationForm, UserChangeForm
# # from .models import User
# #
# # def user_list(request):
# #     users = User.objects.all()
# #     return render(request, 'user/user_list.html', {'users': users})
# #
# # def user_create(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('user_list')
# #     else:
# #         form = UserCreationForm()
# #     return render(request, 'user/user_form.html', {'form': form, 'form_title': 'Add User'})
# #
# # def user_edit(request, pk):
# #     user = get_object_or_404(User, pk=pk)
# #     if request.method == 'POST':
# #         form = UserChangeForm(request.POST, instance=user)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('user_list')
# #     else:
# #         form = UserChangeForm(instance=user)
# #     return render(request, 'user/user_form.html', {'form': form, 'form_title': 'Edit User'})
# #
# # def user_delete(request, pk):
# #     user = get_object_or_404(User, pk=pk)
# #     if request.method == 'POST':
# #         user.delete()
# #         return redirect('user_list')
# #     return render(request, 'user/user_confirm_delete.html', {'user': user})
#
