# The nibOS website and manual. Needs Zola 0.23 (brew install zola, or https://www.getzola.org).
#   make          build the site into public/ (every internal link and anchor checked)
#   make serve    build and serve it at http://127.0.0.1:1111, rebuilt on every change
#   make check    the build's checks, and every external link
#   make clean    remove public/
.PHONY: build serve check clean
build:
	zola build
serve:
	zola serve
check:
	zola check
clean:
	rm -rf public
