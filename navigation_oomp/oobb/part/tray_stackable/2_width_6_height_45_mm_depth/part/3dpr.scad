$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-10.0000000000, 40.0000000000, 0]) {
				cylinder(h = 45, r = 5);
			}
			translate(v = [10.0000000000, 40.0000000000, 0]) {
				cylinder(h = 45, r = 5);
			}
			translate(v = [-10.0000000000, -40.0000000000, 0]) {
				cylinder(h = 45, r = 5);
			}
			translate(v = [10.0000000000, -40.0000000000, 0]) {
				cylinder(h = 45, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 1.2000000000]) {
			hull() {
				translate(v = [-10.0000000000, 40.0000000000, 0]) {
					cylinder(h = 43.8000000000, r = 3.8000000000);
				}
				translate(v = [10.0000000000, 40.0000000000, 0]) {
					cylinder(h = 43.8000000000, r = 3.8000000000);
				}
				translate(v = [-10.0000000000, -40.0000000000, 0]) {
					cylinder(h = 43.8000000000, r = 3.8000000000);
				}
				translate(v = [10.0000000000, -40.0000000000, 0]) {
					cylinder(h = 43.8000000000, r = 3.8000000000);
				}
			}
		}
		#translate(v = [0.0000000000, -30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
		#cylinder(h = 1.2000000000, r = 1.8000000000);
		#translate(v = [0.0000000000, 30.0000000000, 0]) {
			cylinder(h = 1.2000000000, r = 1.8000000000);
		}
	}
}