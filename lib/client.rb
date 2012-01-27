require 'rbcurse'
require 'logger'

class Client

  attr_accessor :window

  def initialize
    VER::start_ncurses
    @window = VER::Window.root_window
    run
  end

  def run
    while true do
    end
  end

end

if __FILE__ == $0
  Client.new
end
