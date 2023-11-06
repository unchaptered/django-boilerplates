from routes.dynamic_router import DynamicRouter
from routes.sample.sample_controller import SampleController
from routes.kevin.kevin_controller import KevinController

urlpatterns = DynamicRouter(controllers=[
    SampleController,
    KevinController
]).convertUrlpattenrs()
