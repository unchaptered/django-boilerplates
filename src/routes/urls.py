from routes.dynamic_router import DynamicRouter
from routes.sample.sample_controller import SampleController
from routes.sample.kevin_controller import KevinController

urlpatterns = DynamicRouter(controllers=[
    SampleController,
    KevinController
]).convertUrlpattenrs()
