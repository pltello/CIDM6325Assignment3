from django.contrib import admin
from degree_checklist.models import (Student, Degree, Core_Requirements,
                                     University_Requirements, Department_Requirements,
                                     Major_Requirements)
# Register your models here.
admin.site.register(Student)
admin.site.register(Degree)
admin.site.register(Core_Requirements)
admin.site.register(University_Requirements)
admin.site.register(Department_Requirements)
admin.site.register(Major_Requirements)
