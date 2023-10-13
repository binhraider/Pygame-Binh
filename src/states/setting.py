from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets

class Setting(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background_setting)
    
    def __init_state__(self):
        super().__init_state__()
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.title = Text(
            position=Vector2(screenWidth//2, 50),
            size=Vector2(30, 30),
            text=S().all_settings,
            font_size=80
        )
        
        self.chooseLanguageTitle = Text(
            position=Vector2(4*screenWidth//5, 200),
            size=Vector2(30, 30),
            text= S().setting_language,
            font_size=50,
        )
        
        self.viOption = ImageButtonWithIcon(
            position=Vector2(800, 250),
            background=Assets.tt_background_setting_button,
            icon=Assets.tt_flag_vi,
            text=S().setting_language_vi,
            callback= lambda:self.change_language('vi'),
            font_size=22
        )
        
        self.enOption = ImageButtonWithIcon(
            position=Vector2(1000, 250),
            background=Assets.tt_background_setting_button,
            icon=Assets.tt_flag_uk,
            text=S().setting_language_en,
            callback= lambda:self.change_language('en'),
            font_size=22
        )
        
        self.backButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 600),
            background=Assets.tt_background_setting_button,
            text=S().all_back,
            callback= self.onClickBack,
            font_size=28,
            scale=1.5
        )
        
        self.toggleMusicTitle = Text(
            position=Vector2(screenWidth//5, screenHeight//4),
            size=Vector2(30, 30),
            text= S().setting_music_toggle,
            font_size=40,
        )
        
        self.toggleAudioTitle = Text(
            position=Vector2(screenWidth//5, screenHeight//4 + 100),
            size=Vector2(30, 30),
            text= S().setting_audio_toggle,
            font_size=40,
        )
        
        self.toggleMusicButton = CheckBox(
            position=Vector2(screenWidth//5 + 80, screenHeight//4),
            size=Vector2(50, 50),
            selected_src=Assets.tt_background_setting_toggle_music_on,
            unselected_src=Assets.tt_background_setting_toggle_music_off,
            callback= self.onToggleMusic
        )
        
        self.toggleAudioButton = CheckBox(
            position=Vector2(screenWidth//5 + 120, screenHeight//4 + 100),
            size=Vector2(50, 50),
            selected_src=Assets.tt_background_setting_toggle_audio_on,
            unselected_src=Assets.tt_background_setting_toggle_audio_off,
            callback= self.onToggleAudio
        )
        
        self.widget_group.add(self.title)
        self.widget_group.add(self.chooseLanguageTitle)
        self.widget_group.add(self.toggleMusicTitle)
        self.widget_group.add(self.toggleAudioTitle)
        self.widget_group.add(self.viOption)   
        self.widget_group.add(self.enOption)
        self.widget_group.add(self.backButton)
        self.widget_group.add(self.toggleMusicButton)
        self.widget_group.add(self.toggleAudioButton)
        
    
    def change_language(self, langueCode):
        S.language = langueCode
    
    def onClickBack(self):
        StateMachine.pop()
        
    def onToggleMusic(self, selected: bool):
        print(f"Music is {selected}")
        
    def onToggleAudio(self, selected: bool):
        print(f"Audio is {selected}")