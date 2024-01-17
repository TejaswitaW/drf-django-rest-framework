from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self,request,view):
        # even authenticated person is not allowed to perform write operation      
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
            
class IsGETOrPatch(BasePermission):
    def has_permission(self,request,view):
        # allow only GET and PATCH
        safe_methods = ['GET','PATCH']
        if request.method in safe_methods:
            return True
        else:
            return False
        
class MaryPermission(BasePermission):
    def has_permission(self,request,view):
        username = request.user.username
        if username.lower() == 'mary':
            return True
        elif username != '' and len(username)%2 == 0 and request.method in SAFE_METHODS:
            return True
        else:
            False

