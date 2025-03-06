$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-70.0000000000, 70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [70.0000000000, 70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [-70.0000000000, -70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [70.0000000000, -70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 1.2000000000]) {
			hull() {
				translate(v = [-70.0000000000, 70.0000000000, 0]) {
					cylinder(h = 16.8000000000, r = 3.8000000000);
				}
				translate(v = [70.0000000000, 70.0000000000, 0]) {
					cylinder(h = 16.8000000000, r = 3.8000000000);
				}
				translate(v = [-70.0000000000, -70.0000000000, 0]) {
					cylinder(h = 16.8000000000, r = 3.8000000000);
				}
				translate(v = [70.0000000000, -70.0000000000, 0]) {
					cylinder(h = 16.8000000000, r = 3.8000000000);
				}
			}
		}
		#translate(v = [-60.0000000000, -60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-60.0000000000, -30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-60.0000000000, 0.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-60.0000000000, 30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-60.0000000000, 60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-30.0000000000, -60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-30.0000000000, -30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-30.0000000000, 0.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-30.0000000000, 30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-30.0000000000, 60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [0.0000000000, -60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [0.0000000000, -30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#cylinder(h = 1.2000000000, r = 1.8000000000);
		#translate(v = [0.0000000000, 30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [0.0000000000, 60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [30.0000000000, -60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [30.0000000000, -30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [30.0000000000, 0.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [30.0000000000, 30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [30.0000000000, 60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [60.0000000000, -60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [60.0000000000, -30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [60.0000000000, 0.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [60.0000000000, 30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [60.0000000000, 60.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
	}
}