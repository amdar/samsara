import characters as c
character = c.Character("The nameless one", "Who am I?", [])

import area_generation as ag

tile_catalog = []
tile_catalog.append({"name":"Granite wall",
				"desc":"Description of granite wall",
				"char":"#",
				"is_solid":True})
tile_catalog.append({"name":"Granite floor",
				"desc":"Description of granite floor",
				"char":".",
				"is_solid":False})
tile_catalog.append({"name":"Gnarly tree",
				"desc":"Description of a tree",
				"char":"T",
				"is_solid":False})
				
area_catalog = []
area_catalog.append({
	"name":"An area",
	"desc":"Description of an area",
	"size_x":128,
	"size_y":128,
	"size_z":1
})

areas = []
areas.append(ag.Area(area_catalog[0]["name"], area_catalog[0]["desc"], area_catalog[0]["size_x"], area_catalog[0]["size_y"], area_catalog[0]["size_z"]))
