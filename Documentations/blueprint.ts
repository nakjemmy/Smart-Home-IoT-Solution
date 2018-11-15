class Device {
	id: number;
	name: string;
	description: string;
}

class Setup {
	id: number;
	name: string;
	room_id: number;
	devices: Device[];
}

class Room {
	id: number;
	name: string;
	house_id: number;
}

class House {
	id: number;
	name: string;
}

class System {
	id: number;
	house_id: number;
}

class Schedule {
	id: number;
	house_id: number;
	configurations: Configuration[];
}

class Configuration {
	id: number;
	start_time: timestamp;
	end_time: timestamp;
}