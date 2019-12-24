from django.contrib import admin
from .models import Questions,Choices
from django.utils.html import format_html
# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choices


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    """
    创建 question 模型后台
    """
    list_display = ("question_text","pub_date")
    search_fields = ("questions_text",)
    inlines = [ChoiceInline]

    pass
@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    """
    创建 question 模型后台
    """
    def list_votes(self,obj):
        return  format_html('<div style="color:red">%s</div>'%(str(obj.votes)+"个"))
    # filter("choice_text") # x显示哪些字段
    list_display = ("choice_text", "list_votes",'votes')
    search_fields = ("choice_text",)
    list_filter= ('question',)


