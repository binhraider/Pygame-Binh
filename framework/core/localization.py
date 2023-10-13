from framework.core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
    languages = {'vi', 'en'}
    strings = {'en': {'all_settings': 'Settings', 'setting_language': 'Language', 'all_back': 'Back', 'all_menu': 'Menu', 'all_quit': 'Quit',  'all_setting': 'Setting', 'all_credits': 'Credits', 'all_play': 'Play', 'all_score': 'Score', 'setting_audio_toggle': 'Audio Effects', 'setting_music_toggle': 'Music', 'all_play': 'Play', 'setting_language_en': 'English', 'setting_language_vi': 'Vietnamese'}, 'vi': {'all_menu':'Menu', 'all_play':'Chơi', 'all_credits': 'Bản quyền', 'all_setting': 'Cài đặt', 'all_quit': 'Thoát', 'all_score': 'Điểm', 'all_settings': 'Cài đặt', 'all_back': 'Quay lại', 'setting_audio_toggle': 'Hiệu ứng âm thanh', 'setting_music_toggle': 'Âm nhạc', 'setting_language': 'Ngôn ngữ', 'setting_language_en': 'Tiếng Anh', 'setting_language_vi': 'Tiếng Việt'}}
    
    @property
    def all_settings(self):
        return Localization.strings[Localization.language]['all_settings']
    
    @property
    def all_back(self):
        return Localization.strings[Localization.language]['all_back']
    
    @property
    def all_menu(self):
        return Localization.strings[Localization.language]['all_menu']
    
    @property
    def all_quit(self):
        return Localization.strings[Localization.language]['all_quit']
    
    @property
    def all_score(self):
        return Localization.strings[Localization.language]['all_score']
    
    @property
    def all_setting(self):
        return Localization.strings[Localization.language]['all_setting']
    
    @property
    def all_credits(self):
        return Localization.strings[Localization.language]['all_credits']
    
    @property
    def setting_audio_toggle(self):
        return Localization.strings[Localization.language]['setting_audio_toggle']
    
    @property
    def setting_music_toggle(self):
        return Localization.strings[Localization.language]['setting_music_toggle']
    
    @property
    def setting_language(self):
        return Localization.strings[Localization.language]['setting_language']
    
    @property
    def all_play(self):
        return Localization.strings[Localization.language]['all_play']
    
    @property
    def setting_language_en(self):
        return Localization.strings[Localization.language]['setting_language_en']
    
    @property
    def setting_language_vi(self):
        return Localization.strings[Localization.language]['setting_language_vi']
    