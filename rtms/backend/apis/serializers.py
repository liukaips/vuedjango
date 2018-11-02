from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone



from backend.models import Case, Result, Flow, Suite, Auth, AuthScript1, Plan,UserInfo
from backend.tasks import cook_plan

class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='userprofile.phone', allow_blank=True, required=False)
    checkPass = serializers.CharField(write_only=True)

    class Meta:
            model = User
            fields = ('id', 'username', 'first_name', 'email', 'phone', 'checkPass')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['checkPass'])
        user.save()
        return user

class UserInfoSerializer(serializers.ModelSerializer):
    birth = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address  = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
            model = UserInfo
            fields = ( 'birth','name', 'address')



class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = ('id', 'name')


class CaseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Case
            fields = ('id', 'name', 'url', 'cookies', 'header', 'boby', 'remark', 'retId', 'expect')


class ResultSerializer(serializers.ModelSerializer):
        class Meta:
            model = Result
            fields = ('id', 'caseId', 'resultall', 'resultId', 'ret')


class FlowSerializer(serializers.ModelSerializer):
        class Meta:
            model = Flow
            fields = ('id', 'name', 'cards', 'flowRemark')


class SuiteSerializer(serializers.ModelSerializer):

        class Meta:
            model = Suite
            fields = ('id', 'casesuite', 'flowId')


class AuthSerializer(serializers.ModelSerializer):
        class Meta:
            model = Auth
            fields = ('id', 'auths', 'authCase')


class AuthScript1Serializer(serializers.ModelSerializer):
        class Meta:
            model = AuthScript1
            fields = ('id', 'name', 'auth_jar')


class PlanScriptSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Plan
            fields = ('id', 'name', 'flag', 'execute_time', 'frikcy', 'cases_id', 'switch', 'create_time', 'period')

        def create(self, validated_data):
            plan = Plan.objects.create(**validated_data)
            if validated_data['flag'] != 'A':
                cook_plan(plan.id)
            return plan

