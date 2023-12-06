
from .permissions import IsStaffEditor
from rest_framework.permissions import IsAdminUser
class StaffEditorMixin():
    permission_classes = [IsAdminUser,IsStaffEditor]