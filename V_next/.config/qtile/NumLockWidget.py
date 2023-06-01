
class NumLockWidget(base._Widget):
    """
    summary:
    Widget to display NumLock status as an Image
    """

    defaults = [
        #("music_players", [{}], "list of all media players including their name and text color"),
        #("song_name", None, "current song name from current running media player"),
    ]

    #current_running_media_player = ""
    #current_song_metadata = {}

    def __init__(self):
        base._Widget.__init__(self)
        self.add_defaults(NumLockWidget.defaults)


    def _configure(self, qtile, bar):
        base._Widget._configure(self, qtile, bar)
        
        # set the song info text
        self.set_current_running_media_player()
        self.set_current_song_metadata()

        # set the song cover image
        self._update_cover_path(self.get_current_song_metadata("artUrl"), self.current_running_media_player)
        self._update_cover_image()

        self.textlayout = self.drawer.textlayout(
            text=self.format_song_info_str(),
            colour="FFFFFF",
            font_family=self.font_family,
            font_size=12,
            font_shadow=None,
            markup=True,
        )

    def _update_cover_image(self):
        self.img = None

        if not self.cover_path:
            return

        self.cover_path = os.path.expanduser(self.cover_path)

        if not os.path.exists(self.cover_path):
            return

        img = Img.from_path(self.cover_path)
        self.img = img
        img.theta = self.rotate
        if not self.scale:
            return
        if self.bar.horizontal:
            new_height = self.bar.height - (self.margin_y * 2)
            img.resize(height=new_height)
        else:
            new_width = self.bar.width - (self.margin_x * 2)
            img.resize(width=new_width)


   def draw(self):
        if self.img is None:
            return

        # draw the song cover image
        self.drawer.clear(self.background or self.bar.background)
        self.drawer.ctx.save()
        self.drawer.ctx.translate(self.margin_x, self.margin_y)
        self.drawer.ctx.set_source(self.img.pattern)
        self.drawer.ctx.paint()
        self.drawer.ctx.restore()
        
        # draw the song information text
        self.textlayout.draw(35, 0)

        if self.bar.horizontal:
            self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.width)
        else:
            self.drawer.draw(offsety=self.offset, offsetx=self.offsetx, height=self.width)


   def calculate_length(self):
        # === NOTE ===
        # for time being, the width is fixed. I have not figured out the logic yet
        if self.cover_path:
            return 400
        else:
            return 0

    def _update_cover_path(self, cover_url, media_player_name):
        if self.get_current_song_metadata("title") != '':
            # first check if the covers folder does exist in the first place, if not then create a new one
            if not os.path.exists(self.covers_folder):
                os.makedirs(self.covers_folder)
            
            if self.current_running_media_player == "Lollypop":
               self.cover_path = self.get_current_song_metadata("artUrl")[7:]
            elif media_player_name == "spotify" or media_player_name == "Deezer":
                # check if song cover had been downloaded before, then just set the path to it
                if os.path.exists(f'{self.covers_folder}/{self.get_current_song_metadata("title")} - {self.get_current_song_metadata("artist")}.png'):
                    self.cover_path = f'{self.covers_folder}/{self.get_current_song_metadata("title")} - {self.get_current_song_metadata("artist")}.png'
                # if not, download the song cover
                else:
                    r = requests.get(cover_url)
                    with open(f'{self.covers_folder}/{self.get_current_song_metadata("title")} - {self.get_current_song_metadata("artist")}.png', 'wb') as f:
                        f.write(r.content)
                    self.cover_path = f'{self.covers_folder}/{self.get_current_song_metadata("title")} - {self.get_current_song_metadata("artist")}.png'

    def get_media_player_status(self, player_name):
        return str(subprocess.run(
            ["playerctl", f"--player={player_name}", "status"], capture_output=True, text=True).stdout).rstrip()

    def set_current_running_media_player(self):
        "sets the first playing media player, make sure there is only one media player playing"
        for player in self.music_players:
            if self.get_media_player_status(player['name']) == "Playing":
                self.current_running_media_player = player['name']
                break

    def get_current_running_media_player_info(self):
        ''''
        returns the media player dictionary (including name and text color)
        ex. {'name': 'spotify', color': '#A0F2BD'}
        '''
        for player in self.music_players:
            if player['name'] == self.current_running_media_player:
                return player

    def set_current_song_metadata(self):
        '''
        there is no command in playerctl to get the artUrl directly, So I had to get the complete metadate string and then slice it up manually
        '''

        # get the entire metadata string for currently playing media player
        metadata_str = str(subprocess.run(
            ["playerctl", "-p", f"{self.current_running_media_player}", "metadata"], capture_output=True, text=True).stdout).rstrip()

        # slice the string and store each piece of information as a separate item them, and at the end store them in a dictionary
        metadata_dict = {}
        for key in ["title", "artist", "artUrl"]:
            try:
                metadata_dict[key] = metadata_str.split(key, 1)[1].partition(f"{self.current_running_media_player[:5]}")[0].strip()
            except:
                metadata_dict[key] = ""

        self.current_song_metadata = metadata_dict


    def get_current_song_metadata(self, info=None):
        if info == None:
            return self.current_song_metadata
        else:
            return self.current_song_metadata[info]

   