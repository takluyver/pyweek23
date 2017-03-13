build_dir = build/flatpak
app_name = io.github.lukevp.pyweek23

build-flatpak: Makefile
	# Main build steps - set up $(build_dir) and build the app in it.
	rm -rf $(build_dir)
	flatpak build-init --base=org.pygame.BaseApp-py27 $(build_dir)  $(app_name) \
				org.freedesktop.Sdk org.freedesktop.Platform 1.4
	flatpak build $(build_dir) make build-install
	flatpak build-finish $(build_dir) --socket=x11 --socket=pulseaudio --command=solarflair

export-flatpak-repo: build-flatpak
	# Export the build directory into a repo (the source for installation)
	flatpak build-export repo $(build_dir)

uninstall-flatpak:
	# If uninstalling fails, assume it's not installed and continue
	flatpak --user uninstall $(app_name) || true

install-flatpak: export-flatpak-repo uninstall-flatpak repo-added
	flatpak --user install pyweek23-local-repo $(app_name)

repo-added:
	flatpak --user remote-add --no-gpg-verify --if-not-exists pyweek23-local-repo repo

build-install:
	# This is run inside the build environment
	# It installs the files for the application into /app
	mkdir /app/share/solarflair
	cp -r lib /app/share/solarflair/
	cp -r assets /app/share/solarflair/
	cp -r highscores.txt /app/share/solarflair/
	cp -r main.py /app/share/solarflair/
	ln -s /app/share/solarflair/main.py /app/bin/solarflair
	mkdir -p /app/share/applications
	cp $(app_name).desktop /app/share/applications/
	
	for size in 64 ; do \
		install -TD assets/images/star_$${size}.png \
			/app/share/icons/hicolor/$${size}x$${size}/apps/$(app_name).png ; \
	done
