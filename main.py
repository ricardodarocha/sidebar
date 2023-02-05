import flet
from flet import *
from functools  import partial
import time

# Sidebar class
class ModernNavBar(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()

    # Quando passa o mouse por cima dos itens do menu ele destaca os itens selecionados
    def Highlight(self, e):
        if e.data == 'true':
            e.control.bgcolor= 'white10'
            e.control.content.controls[0].icon_color = 'white'
            e.control.content.controls[1].color = 'white'
            e.control.content.update()
        else:
            e.control.bgcolor=None
            e.control.content.controls[0].icon_color = 'white54'
            e.control.content.controls[1].color = 'white54'
            e.control.content.update()
        e.control.update()

    # Este cartão possui os dados do usuário, como ícone, nome e profissão
    def UserData(self, initials: str, name: str, description: str):
        return Container(
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
        
    # Cada item do menu é um containedIcon        
    def ContainedIcon(self, icon_name: str, text: str):
        return  Container(
            width=180,
            height=40,
            border_radius=4,
            on_hover=lambda e: self.Highlight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=8),      
                            },
                            overlay_color={"": "transparent"},
                            )
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                    ),
                ]
            )
        )
    
    # O construtor do SideBar
    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment='center',
                controls=[
                self.UserData("Ri", "Ricardo da Rocha", "designer"),
                    Container(
                    border_radius=16,
                    content=IconButton(
                        icon=icons.SWITCH_LEFT_SHARP,
                        icon_size=12,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            overlay_color={"": "transparent"},
                        )
                    ),
                    width=30, 
                    height=30, 
                    bgcolor="black", 
                    on_click=partial(self.func),
                    ),
                Divider(height=5, color="transparent"),
                self.ContainedIcon(icons.SEARCH, 'Buscar'),
                Divider(height=5, color="white24"),
                self.ContainedIcon(icons.HOME_OUTLINED, 'Home'),
                self.ContainedIcon(icons.NOTIFICATIONS, 'Alertas'),
                self.ContainedIcon(icons.WALLET_ROUNDED, 'Carteira'),
                self.ContainedIcon(icons.BAR_CHART, 'Resultados'),
                Divider(height=5, color="white24"),
                self.ContainedIcon(icons.FAVORITE_ROUNDED, 'Favoritos'),
                self.ContainedIcon(icons.SETTINGS_BRIGHTNESS_OUTLINED, 'Configurações'),
                Divider(height=5, color="white24"),
                self.ContainedIcon(icons.LOGOUT_ROUNDED, 'Sair'),
            ]))
    
def main(page: Page):
    page.title = "Ricardo da Rocha inc"
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.bgcolor='#212121'

    def AnimateSidebar(e):
        if page.controls[0].width != 62:

            for item in (
            page.controls[0]
            .content.controls[0]
            .content.controls[0]
            .content.controls[1]
            .controls[:]
            ):
                item.opacity = (0)
                item.update()

            for item in (
            page.controls[0]
            .content.controls[0]
            .content.controls[3:]
            ):
                if isinstance(item, Container):
                    item.content.controls[1].opacity = 0
                    item.content.update()

            time.sleep(0.2)

            page.controls[0].width = 62
            page.controls[0].update()
        else:
            page.controls[0].width = 200
            time.sleep(0.2)
            for item in (
                page.controls[0]
                .content.controls[0]
                .content.controls[0]
                .content.controls[1]
                .controls[:]
            ):
                item.opacity = (1)
                item.update()
            
            for item in (
                page.controls[0]
                .content.controls[0]
                .content.controls[3:]
            ):
                if isinstance(item, Container):
                    item.content.controls[1].opacity = 1
                    item.content.update()


            page.controls[0].update()


    page.add(
        Container(
            width=300,    
            height=600,    
            bgcolor=colors.BLACK38,
            border_radius=10,
            alignment=alignment.center,
            animate=animation.Animation(500, 'decelerate'),
            padding=10,
            content=ModernNavBar(AnimateSidebar)
        )
    )

    page.update()

if __name__ == '__main__':
    flet.app(target=main)
