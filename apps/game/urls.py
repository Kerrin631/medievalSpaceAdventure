from django.conf.urls import patterns, url
from . import views
from views import StartGet, StartPost, MountainsGet, MountainsPost, ColdRoomGet, ColdRoomPost, PrisonHallGet, PrisonHallPost, OpenRoomGet, OpenRoomPost, SphinxLairGet, SphinxLairPost, SpaceRoomGet, SpaceRoomPost, CypherRoomGet, CypherRoomPost, DragonsLairGet, DragonsLairPost, CockpitGet
# for django 1.9 use from . import views
urlpatterns = patterns('',
  url(r'^$', StartGet.as_view(), name='start'),
  url(r'^postDirector/$', views.postDirector, name='postDirector'),
  url(r'^newGame/$', views.newGame, name='newGame'),
  url(r'^startPost/$', StartPost.as_view(), name='startPost'),
  url(r'^mountains/$', MountainsGet.as_view(), name='mountains'),
  url(r'^mountainsPost/$', MountainsPost.as_view(), name='mountainsPost'),
  url(r'^coldRoom/$', ColdRoomGet.as_view(), name='ColdRoom'),
  url(r'^coldRoomPost/$', ColdRoomPost.as_view(), name='ColdRoomPost'),
  url(r'^prisonHall/$', PrisonHallGet.as_view(), name='prisonHall'),
  url(r'^prisonHallPost/$', PrisonHallPost.as_view(), name='prisonHallPost'),
  url(r'^openRoom/$', OpenRoomGet.as_view(), name='openRoom'),
  url(r'^openRoomPost/$', OpenRoomPost.as_view(), name='openRoomPost'),
  url(r'^sphinxLair/$', SphinxLairGet.as_view(), name='sphinxLair'),
  url(r'^sphinxLairPost/$', SphinxLairPost.as_view(), name='sphinxLairPost'),
  url(r'^spaceRoom/$', SpaceRoomGet.as_view(), name='spaceRoom'),
  url(r'^spaceRoomPost/$', SpaceRoomPost.as_view(), name='spaceRoomPost'),
  url(r'^cypherRoom/$', CypherRoomGet.as_view(), name='cypherRoom'),
  url(r'^cypherRoomPost/$', CypherRoomPost.as_view(), name='cypherRoomPost'),
  url(r'^dragonsLair/$', DragonsLairGet.as_view(), name='dragonsLair'),
  url(r'^dragonsLairPost/$', DragonsLairPost.as_view(), name='dragonsLairPost'),
  url(r'^cockpit/$', CockpitGet.as_view(), name='cockpit')
)