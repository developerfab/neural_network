# Neuron class

class Neuron
  def initialize(weights, activate_value)
    @weight = 0
    @activate_value = activate_value
    @new_weight = 0
    calcule_weight(weights)
  end

  def calcule_weight(weights)
    weights.each do |w|
      @weight = @weight + w
    end
  end

  def activate
    if @weight > 0
      @new_weight = @weight * @activate_value
    end
    puts @new_weight
  end
end

start = Time.now
weights = [10,20,30,40,50]
neuron2 = Neuron.new(weights, 2)
neuron2.activate
stop = Time.now
puts stop - start
