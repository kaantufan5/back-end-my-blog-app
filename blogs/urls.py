from rest_framework import routers
from .views import (
    CategoryView,
    PostView,
    CommentView,
    LikeView,
    PostDetView
)

router = routers.DefaultRouter()

router.register("categories", CategoryView)
router.register("posts", PostView)
router.register("comments", CommentView)
router.register("likes", LikeView)
router.register("postdets", PostDetView)

urlpatterns = [

]

urlpatterns += router.urls
