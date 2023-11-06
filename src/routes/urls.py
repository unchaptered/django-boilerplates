from routes.dynamic_router import DynamicRouter
from routes.sample.sample_controller import SampleController

urlpatterns = DynamicRouter(controllers=[SampleController]).convertUrlpattenrs()
print(urlpatterns)