"""This file defines a renderable type class and all data classes that extend this typeclass.
Data classes extending the type class can be used to produce documents (pdfs/images/...)"""

from classes import AssociatedType, Supports, typeclass




class Renderable(AssociatedType):
    """Special type to represent that some instance can be `rendert`."""

@typeclass(Renderable)
def render(instance) -> str:
    """No implementation needed."""




#make the string class extend the printable typeclass
@render.instance(str)
def _render_str(instance: str) -> str:
    return 'Hello, {0}!'.format(instance)




#create a function that uses Renderable objects
def greet_and_print(instance: Supports[Renderable]) -> None:
    print(render(instance))

greet_and_print("hallo")
