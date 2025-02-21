from rest_framework import permissions

# TODO Tests
class IsBlogOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.author == obj.author
