$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-25.0000000000, 55.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [25.0000000000, 55.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [-25.0000000000, -55.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [25.0000000000, -55.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 1.2000000000]) {
			hull() {
				translate(v = [-25.0000000000, 55.0000000000, 0]) {
					cylinder(h = 22.8000000000, r = 3.8000000000);
				}
				translate(v = [25.0000000000, 55.0000000000, 0]) {
					cylinder(h = 22.8000000000, r = 3.8000000000);
				}
				translate(v = [-25.0000000000, -55.0000000000, 0]) {
					cylinder(h = 22.8000000000, r = 3.8000000000);
				}
				translate(v = [25.0000000000, -55.0000000000, 0]) {
					cylinder(h = 22.8000000000, r = 3.8000000000);
				}
			}
		}
		#translate(v = [-15.0000000000, -45.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-15.0000000000, -15.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-15.0000000000, 15.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [-15.0000000000, 45.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [15.0000000000, -45.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [15.0000000000, -15.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [15.0000000000, 15.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#translate(v = [15.0000000000, 45.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
	}
}