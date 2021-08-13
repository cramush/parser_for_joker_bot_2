
.PHONY: parse
parse:
	docker build ./parser -f parser/Dockerfile.parser -t parser_2
	docker run -it --network joker_network parser_2
