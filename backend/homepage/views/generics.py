from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from homepage.serializers import ProfileSerializer
from homepage.models import Profile
from user.serializers import UserSerializer
from post.serializers import PostSerializer


class ProfilesAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    # ok


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # ok


class ProfileFollowingAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return Profile.objects.get(id=self.request['pk']).following.all()
    # Refactor logic


class ProfileFollowersAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return Profile.objects.get(id=self.request['pk']).followers.all()
    # Refactor logic


class ProfilesPostsAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Profile.objects.get(id=self.kwargs['pk']).posts.all()

    def perform_create(self, serializer):
        profile = Profile.objects.get(id=self.kwargs['pk'])
        return serializer.save(owner=profile)
    # ok


# class ProfilesPostAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         return Profile.objects.get(id=self.kwargs['pk']).posts.get(id=self.kwargs['pk2'])
#
#     # TODO have to be overwritten with cbv
