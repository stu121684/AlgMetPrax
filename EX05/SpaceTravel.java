import java.util.HashSet;
import java.util.Scanner;

public class SpaceTravel {
	
	private static int mst(Point[] planets) {
		int sum = 0;
		HashSet<Integer> used = new HashSet<Integer>();
		SpaceDistance[] dist = new SpaceDistance[planets.length];
		used.add(0);

		for (int i = 1; i < dist.length; i++) {
			dist[i] = (new SpaceDistance(planets[0].distance(planets[i]), i));
		}
		while (used.size() != dist.length) {
			int min = -1;
			int minPos = -1;
			for (int i = 0; i < dist.length; i++) {
				if (!used.contains(i)) {
					if (min == -1 || dist[i].value < min) {
						min = dist[i].value;
						minPos = i;
					}
				}
			}

			used.add(minPos);
			sum += min;
			for (int i = 0; i < dist.length; i++) {
				if (!used.contains(i)) {
					dist[i].value = Math.min(dist[i].value, planets[minPos].distance(planets[i]));
				}
			}
		}
		return sum;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();

			Point[] planets = new Point[n];
			for (int i = 0; i < planets.length; i++) {
					int x = sc.nextInt();
					int y = sc.nextInt();
					int z = sc.nextInt();
					
					planets[i] = new Point(x, y, z);
			}
			
			int res = mst(planets);
			System.out.format("Case #%d: %d\n", tc, res);
		}
		sc.close();
	}

	static class SpaceDistance {
		int value;
		int index;
		SpaceDistance(int dist, int index){
			this.value = dist;
			this.index = index;
		}
		
	}
	
	static class Point {
		int x, y, z;

		Point(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}

		int distance(Point p) {
			int dx = Math.abs(p.x - this.x);
			int dy = Math.abs(p.y - this.y);
			int dz = Math.abs(p.z - this.z);
			return dx + dy + dz;
		}
	}

}
