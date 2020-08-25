from rest_framework import serializers
from .models import lesson
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.models import User


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    title_image = Base64ImageField()
    term1_image = Base64ImageField()
    term2_image = Base64ImageField()
    term3_image = Base64ImageField()
    step1_image = Base64ImageField()
    step2_image = Base64ImageField()
    step3_image = Base64ImageField()
    step4_image = Base64ImageField()
    step5_image = Base64ImageField()
    step6_image = Base64ImageField()
    step7_image = Base64ImageField()
    step8_image = Base64ImageField()

    class Meta:
        model = lesson
        fields = ('global_lesson_id','lesson_id','class_id','user','title','title_image','title_video','title_description',
                  'term1','term1_description','term1_image','term2','term2_description','term2_image','term3','term3_description','term3_image'
                  ,'number_of_steps','step1_description','step1_image','step2_description','step2_image','step3_description','step3_image',
                  'step4_description','step4_image','step5_description','step5_image','step6_description','step6_image','step7_description','step7_image'
                  ,'step8_description','step8_image','questions')


    def validate_user(self,value):
        print(str(dir(value)))
        print(str(value.id))
        lesson_list = lesson.objects.filter(user=value.id)

        print(str(len(lesson_list)))

        if len(lesson_list) > 20:
            raise serializers.ValidationError('The maximum number of lessons for the user is reached')
        else:
            return value

    def validate_title_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of title image is greater than 500 KB')
            else:
                return value
    def validate_title_video(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of title video is greater than 500 KB')
            else:
                return value
    def validate_term1_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of term 1 image is greater than 500 KB')
            else:
                return value
    def validate_term2_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of term 2 image is greater than 500 KB')
            else:
                return value
    def validate_term3_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of term 3 image is greater than 500 KB')
            else:
                return value

    def validate_step1_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 1 image is greater than 500 KB')
            else:
                return value
    def validate_step2_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 2 image is greater than 500 KB')
            else:
                return value
    def validate_step3_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 3 image is greater than 500 KB')
            else:
                return value

    def validate_step4_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 4 image is greater than 500 KB')
            else:
                return value

    def validate_step5_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 5 image is greater than 500 KB')
            else:
                return value
    def validate_step6_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 6 image is greater than 500 KB')
            else:
                return value

    def validate_step7_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 7 image is greater than 500 KB')
            else:
                return value

    def validate_step8_image(self,value):
        if value is not None:
            print("Image"+str(type(value))+str(value.size))
            if value.size > 500000:
                raise serializers.ValidationError('Size of step 8 image is greater than 500 KB')
            else:
                return value
    def create(self, validated_data):
        lesson_id = validated_data.pop('lesson_id')
        class_id = validated_data.pop('class_id')
        user = validated_data.pop('user')
        title = validated_data.pop('title')
        title_image = validated_data.pop('title_image')
        title_video = validated_data.pop('title_video')
        title_description = validated_data.pop('title_description')
        term1 = validated_data.pop('term1')
        term1_description = validated_data.pop('term1_description')
        term1_image = validated_data.pop('term1_image')
        term2 = validated_data.pop('term2')
        term2_description = validated_data.pop('term2_description')
        term2_image = validated_data.pop('term2_image')
        term3 = validated_data.pop('term3')
        term3_description = validated_data.pop('term3_description')
        term3_image = validated_data.pop('term3_image')
        step1_description = validated_data.pop('step1_description')
        step1_image = validated_data.pop('step1_image')
        step2_description = validated_data.pop('step2_description')
        step2_image = validated_data.pop('step2_image')
        step3_description = validated_data.pop('step3_description')
        step3_image = validated_data.pop('step3_image')
        step4_description = validated_data.pop('step4_description')
        step4_image = validated_data.pop('step4_image')
        step5_description = validated_data.pop('step5_description')
        step5_image = validated_data.pop('step5_image')
        step6_description = validated_data.pop('step6_description')
        step6_image = validated_data.pop('step6_image')
        step7_description = validated_data.pop('step7_description')
        step7_image = validated_data.pop('step7_image')
        step8_description = validated_data.pop('step8_description')
        step8_image = validated_data.pop('step8_image')
        questions = validated_data.pop('questions')



        return lesson.objects.create(lesson_id=lesson_id, class_id=class_id,user=user,title=title,title_image=title_image,title_video=title_video,title_description=title_description,
                                     term1=term1,term1_description=term1_description,term1_image=term1_image,term2=term2,term2_description=term2_description,term2_image=term2_image,term3=term3,term3_description=term3_description,term3_image=term3_image,
                                     step1_description=step1_description,step1_image=step1_image,step2_description=step2_description,step2_image=step2_image,step3_description=step3_description,step3_image=step3_image,step4_description=step4_description,step4_image=step4_image,
                                     step5_description=step5_description,step5_image=step5_image,step6_description=step6_description,step6_image=step6_image,step7_description=step7_description,step7_image=step7_image,step8_description=step8_description,step8_image=step8_image,questions=questions)

class UserSerializer(serializers.ModelSerializer):
        lessons = serializers.PrimaryKeyRelatedField(many=True, queryset=lesson.objects.all())

        class Meta:
            model = User
            fields = ['id', 'username', 'lessons']