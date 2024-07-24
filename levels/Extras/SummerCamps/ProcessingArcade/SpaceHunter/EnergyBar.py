class EnergyBar:
    regen_rate = 1.0      # bigger => regen energy faster 
    
    width = 600
    height = 170
    bar_width = 450
    bar_segment_width = 25
    bar_segment_end_width = 75
    
    def __init__(self):
        self.image = loadImage('energyBar.png')
        self.image_holder = loadImage('eBarHolder.png')
        self.image_bar = loadImage('energy_segment.png')
        self.image_bar_end = loadImage('energy_end.png')
        
        self.image_holder.resize(170, 170)
        self.image_bar.resize(EnergyBar.bar_segment_width, 120)
        self.image_bar_end.resize(EnergyBar.bar_segment_end_width, 120)
        
        max_energy_bars = (EnergyBar.bar_width - EnergyBar.bar_segment_end_width) / EnergyBar.bar_segment_width
        self.energy_per_bar = floor(100 / max_energy_bars)
        
        # Lose 1 energy bars per shot--configurable
        self.energy_per_shot = self.energy_per_bar
        
        # Only regen after not shooting for a specific time
        # Prevents spamming the mouse for shooting
        self.regen_delay_ms = 500
        self.regen_timer_ms = None 
        
        self.amount_of_energy = 100
        
        
    def draw(self):
        push()
        
        center_x = int( 10 + (EnergyBar.width/2) )
        center_y = int( height - 30 - (EnergyBar.height/2) )
        image(self.image, center_x, center_y)
        
        # Must place after base bar image, but before top holder
        # image to hide energy bar edge
        bar_x = center_x - EnergyBar.width/4
        bar_y = center_y - ((19*EnergyBar.height)/100)
        num_bars = int(self.amount_of_energy / self.energy_per_bar)
        
        for i in range(num_bars):
            image(self.image_bar, bar_x + (i * EnergyBar.bar_segment_width), bar_y)
        image(self.image_bar_end, bar_x + ((num_bars + 1) * EnergyBar.bar_segment_width), bar_y)
        
        # The circular cap with the lightning bolt--place after drawing
        # the energy bar to hide the bar's edge
        image(self.image_holder, center_x - ((35*EnergyBar.width)/100), center_y)
        
        fill(0)
        textSize(48)
        text( str(self.amount_of_energy) + '/ 100', center_x, center_y + 70 )
        
        if self.regen_timer_ms is not None:
            if millis() - self.regen_timer_ms > self.regen_delay_ms:
                self.amount_of_energy += EnergyBar.regen_rate
                if self.amount_of_energy > 100:
                    self.amount_of_energy = 100
        
        pop()
        
    def is_enough_energy_for_shot(self):
        return self.amount_of_energy >= self.energy_per_shot
        
    def shot_fired(self):
        self.amount_of_energy -= self.energy_per_shot

        if self.amount_of_energy < 0:
            self.amount_of_energy = 0
            
        self.regen_timer_ms = millis()
    
