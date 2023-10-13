from framework.framework import *
from src.configs.assets import Assets

class Player(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(20, 40), position=position, size=Vector2(85, 64), offset=Vector2(33, 10))
        self.orientation = 'opposite'
        self.show_hitbox = True
        self.speed = 3
        self.alive = True
        self.animation_manager = AnimationManager(
            action_animation = {
                "die": ActionAnimation(entity=self, src=Assets.ani_die, delay=3, frame_count=3),
                'attack_opposite': ActionAnimation(entity=self, src=Assets.ani_attack_opposite, delay=3, frame_count=4),
                'attack_behind': ActionAnimation(entity=self, src=Assets.ani_attack_behind, delay=3, frame_count=4),
                'attack_left': ActionAnimation(entity=self, src=Assets.ani_attack_left, delay=3, frame_count=4),
                'attack_right': ActionAnimation(entity=self, src=Assets.ani_attack_right, delay=3, frame_count=4),
            },
            repeat_animation = {
                'idle_opposite': RepeatAnimation(entity=self, src=Assets.ani_walk_opposite, delay=3, frame_count=6),
                'idle_behind': RepeatAnimation(entity=self, src=Assets.ani_walk_behind, delay=3, frame_count=6),
                'idle_left': RepeatAnimation(entity=self, src=Assets.ani_walk_left, delay=3, frame_count=6),
                'idle_right': RepeatAnimation(entity=self, src=Assets.ani_walk_right, delay=3, frame_count=6),
                'run_opposite': RepeatAnimation(entity=self, src=Assets.ani_run_opposite, delay=3, frame_count=6),
                'run_behind': RepeatAnimation(entity=self, src=Assets.ani_run_behind, delay=3, frame_count=6),
                'run_left': RepeatAnimation(entity=self, src=Assets.ani_run_left, delay=3, frame_count=6),
                'run_right': RepeatAnimation(entity=self, src=Assets.ani_run_right, delay=3, frame_count=6),
                'death': RepeatAnimation(entity=self, src=Assets.ani_die, delay=3, frame_count=1),
            },
            current_animation='idle_opposite'
        )
    
    def __update__(self, event):
        super().__update__(event=event)
        
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.set_position(self.position + Vector2(0, -self.speed))
            self.orientation = 'behind'
            self.animation_manager.change_animation('run_behind')
        elif(keys[pygame.K_s]):
            self.set_position(self.position + Vector2(0, self.speed))
            self.orientation = 'opposite'
            self.animation_manager.change_animation('run_opposite')
        elif(keys[pygame.K_a]):
            self.set_position(self.position + Vector2(-self.speed, 0))
            self.orientation = 'left'
            self.animation_manager.change_animation('run_left')
        elif(keys[pygame.K_d]):
            self.set_position(self.position + Vector2(self.speed, 0))
            self.orientation = 'right'
            self.animation_manager.change_animation('run_right')
        else:
            if(self.alive):
                self.animation_manager.change_animation('idle_' + self.orientation)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.animation_manager.play_action('attack_' + self.orientation)
            if event.key == pygame.K_p:
                self.alive = False
                self.animation_manager.play_action('die')
                self.animation_manager.change_animation('death')

        
