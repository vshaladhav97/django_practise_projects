from import_export import resources
from csvs.models import AmazoneCustomer
class MemberResource(resources.ModelResource):
    class Meta:
        model = AmazoneCustomer