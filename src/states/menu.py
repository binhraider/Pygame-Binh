from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.states.setting import Setting

class Menu(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background_menu)
    
    def __init_state__(self):
        super().__init_state__()

        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y

        self.title = Text(
            position=Vector2(4*screenWidth//8-10, 50),
            size=Vector2(30, 30),
            text=S().all_menu,
            font_size=80
        )
        
        self.playButton = ImageButton(
            position=Vector2(4*screenWidth//10, 170),
            background=Assets.tt_background_menu_button,
            text= S().all_play,
            callback= self.onClickPlay,
            font_size=50,
            scale =1.5
        )


        self.scoreButton = ImageButton(
            position=Vector2(4*screenWidth//10, 290),
            background=Assets.tt_background_menu_button,
            text= S().all_score,
            callback= self.onClickScore,
            font_size=50,
            scale =1.5
        )


        self.creditsButton = ImageButton(
            position=Vector2(4*screenWidth//10, 410),
            background=Assets.tt_background_menu_button,
            text= S().all_credits,
            callback= self.onClickCredits,
            font_size=50,
            scale =1.5
        )

        self.settingButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 530),
            background=Assets.tt_background_menu_button,
            text=S().all_setting,
            callback= self.onClickSetting,
            font_size=50,
            scale=1.5
        )
        
        self.quitButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 650),
            background=Assets.tt_background_menu_button,
            text=S().all_quit,
            callback= self.onClickQuit,
            font_size=50,
            scale=1.5
        )

      
        self.widget_group.add(self.title)
        self.widget_group.add(self.playButton)
        self.widget_group.add(self.scoreButton)
        self.widget_group.add(self.quitButton)
        self.widget_group.add(self.creditsButton)
        self.widget_group.add(self.settingButton)
        
      
    def onClickQuit(self):
        StateMachine.pop()

    def onClickPlay(self):
        StateMachine.pop()
    
    def onClickScore(self):
        StateMachine.pop()

    def onClickCredits(self):
        StateMachine.pop()

    def onClickSetting(self):
        StateMachine.push(Setting())