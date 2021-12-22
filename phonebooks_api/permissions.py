from rest_framework import permissions

class UpdatePhonebook(permissions.BasePermission):
    """Allow the user to edit their own profiles"""
    def has_object_permission(self,request,view,obj):

        if request.method in permissions.SAFE_METHODS:
            """If the method used is a HTTP GET, then it will be in the safe methods, therefore it will just return true and allow the request"""
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id  == request.user.id
