from rest_framework import serializers
from .models import Loan, User


class UserSerializer(serializers.ModelSerializer):
    """integrate user model"""
    class Meta:
        model = User
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    """integrate loan model"""
    class Meta:
        model = Loan
        fields = ('id', 'loan_amount', 'loan_duration', 'rate_of_interest',
                  'interest_amount', 'final_amount', 'loan_limit', 'due_date', 'amt_paid_by_the_bank', 'user_has_to_pay', 'user_id')


class LoanSerializer2(serializers.ModelSerializer):
    """integrate loan model with extended user model"""
    username = serializers.ReadOnlyField(
        source="user_id.username", read_only=True)
    dob = serializers.ReadOnlyField(source="user_id.dob", read_only=True)
    mobile_no = serializers.ReadOnlyField(
        source="user_id.mobile_no", read_only=True)
    pan_no = serializers.ReadOnlyField(source="user_id.pan_no", read_only=True)
    address = serializers.ReadOnlyField(
        source="user_id.address", read_only=True)
    city = serializers.ReadOnlyField(source="user_id.city", read_only=True)
    state = serializers.ReadOnlyField(source="user_id.state", read_only=True)

    class Meta:
        model = Loan
        fields = ('id', 'loan_amount', 'loan_duration', 'rate_of_interest', 'interest_amount', 'final_amount', 'loan_limit',
                  'due_date', 'transaction_date', 'amt_paid_by_the_bank', 'user_has_to_pay', 'user_id', "username", "dob", "mobile_no", "pan_no", "address", "city", "state")
