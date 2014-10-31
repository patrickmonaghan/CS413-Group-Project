class Upload
  include MongoMapper::Document

  key :id, Integer
  key :time_started, Time
  key :fuel_type, String
  key :average_mpg, Integer
  key :distance_traveled, Integer

  many :events
end

class Event
  include MongoMapper::EmbeddedDocument

  key :timestamp, Time
  key :engine_rpm, String
  key :speed, String
  key :engine_coolant_temperature, String
  key :engine_load_value, String
  key :throttle_position, String
  key :ambient_air_temperature, String
  key :latitude, String
  key :longitude, String
  key :consumption, String
end
