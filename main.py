import flet
from flet import *
from functools  import partial
import time

# Sidebar class
class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()

    def UserData(self, initials: str, name: str, description: str):
        return Container(
            bgcolor="bluegrey900",
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="#37474F",
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
                            color="white54"
                        ),
                    ),
                Column(
                    spacing=1,
                    alignment='center',
                    controls=[
                        Text(
                            value=name, 
                            size=12, 
                            weight="bold",
                            color="white54"
                            ),
                        Text(
                            value=description,  
                            size=9, 
                            weight="w400",
                            color="white54"
                            ),
                        ],
                    opacity=1,
                    animate_opacity=200,

                ),
                ]
            )
        )
        
    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(controls=[
            self.UserData("Ri", "Ricardo da Rocha", "designer"),
            ]))
    
def main(page: Page):
    page.title = "Ricardo da Rocha inc"
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.bgcolor='#212121'
    page.add(
        Container(
            width=300,    
            height=600,    
            bgcolor="#263238",
            border_radius=10,
            alignment=alignment.center,
            animate=animation.Animation(500, 'decelerate'),
            padding=10,
            content=ModernNavBar()
        )
    )

    page.update()

if __name__ == '__main__':
    flet.app(target=main)
