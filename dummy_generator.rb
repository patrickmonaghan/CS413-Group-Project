require 'nokogiri'
require 'pry'
require "json"

gpx_data = File.read("ride.gpx")

parser = Nokogiri::XML(gpx_data)

points = parser.children.children[3].children[3].children.map {|c| c.attributes unless c.attributes == {}}.compact

events = []

points.each do |point|
  events << {
    timestamp: "2014-10-28 11:06:02 +0000",
    engine_rpm: rand(1000...5000),
    speed: rand(30..40),
    engine_coolant_temperature: 20,
    engine_load_value: rand(70..100),
    throttle_position: rand(40..100),
    ambient_air_temperature: rand(20..23),
    latitude: point["lat"].value.to_f,
    longitude: point["lon"].value.to_f,
    consumption: rand(45..50)
  }
end

average_mpg = events.map {|e| e[:consumption]}.inject {|sum, el| sum + el} / events.length

data = {
  id: 1,
  time_started: "2014-10-28 11:06:02 +0000",
  fuel_type: "Diesel",
  average_mpg: average_mpg,
  distance_traveled: 100,
  events: events
}

file = File.new("dummy_data.json", "w")
file.write(data.to_json)
file.close