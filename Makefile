# The binary to build (basename).
MODULE := firework

run:
	@python3 $(MODULE)

clean:
	rm -rf logs cache .pytest_cache