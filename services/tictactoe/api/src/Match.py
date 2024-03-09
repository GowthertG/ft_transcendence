import                      asyncio
from    .Player  import     Player
from    .Move    import     Move
from    .Board   import     StateBoard

PENDING     = 0
DRAW        = 1
WIN         = 3
class Match():
    def __init__( self ):
        self.__id               = 0
        self.__room_name        = "" #using player
        self.__state            = "PENDING" # "CONTINUE", #WIN, #LOSE, #DRAW, #PAUSE
        self.__winner           = 0 #id_winner
        self.__players          = {} # { id1:player[0], id2:player[2] }
        self.__owners           = {}
        self.__bot_players      = {}
        self.__manual_players   = {}
        self.__moves            = [ ] #moves
        self.__turn             = 0 # id

        self.__board            = StateBoard()

        self.task_abort         = None

    def add_player( self, id ):
        self.__players[ id ] = Player( id )

    def remove_player( self, id ):
        self.__players.pop( id )

    def status( self ):
        if len( self.__players ) == 2:
            return "PLAYING"
        else:
            return "PENDING"

    async def wait_match( self ):
        await asyncio.sleep( 10 )
        #incst
        #incst
        #incst
        #incst
        #incst
        #incst
        # Can have mutexes
        print("Match abort", flush=True)
        # Matches[ self.__state ].pop( self.__id )
        #end

    async def wait_player( self ):
        await asyncio.sleep( 15 )

        # Can have mutexes
        # Abort the player and the other one win
        # end

    def simulate( self, move_s, player_id ):
        move    = Move( int( move_s[2] ),
                        int( move_s[3] ),
                        int( move_s[0] ),
                        int( move_s[1] ) )
        
        # print( move )
        # print( player_id )

        response = self.__players[ player_id ].simulate( move )

        return response
        
        
                        
