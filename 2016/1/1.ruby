file = File.open("input")
file_data = file.readlines.map(&:chomp)
file.close


position = [0,0]
direction = [1,0]
# move : from <position>, step <walk> times in <direction> 
def move(position,direction,walk)
    finalPosition = []
    for x in 0...position.length()
        finalPosition << position[x]+direction[x]*walk
    end
    return finalPosition
end

#turn <direction> following <angle>
def turn(angle,direction)
    if angle =="R"
        if direction[0]==0
            return[direction[1]*-1,direction[0]]
        else 
            return[direction[1],direction[0]]
        end
    else # L
        if direction[0]==0
            return[direction[1],direction[0]]
        else 
            return[direction[1],direction[0]*-1]
        end
    end
end

file_data[0].split(", ").each do |turn|
    puts "go #{turn}"
    angle = turn[0]
    walk = turn[1..-1].to_i
    direction = turn(angle,direction)
    puts "direction #{direction}"
    position = move(position,direction,walk)
    puts "arrives in #{position}"
    puts ""
    blocks = position[0].abs + position[1].abs
    puts "distance : #{blocks} blocks"
end
