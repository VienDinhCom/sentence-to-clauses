FROM java:jre-alpine

RUN apk add --update --no-cache \
	 unzip \
	 wget

RUN wget http://nlp.stanford.edu/software/stanford-corenlp-latest.zip
RUN unzip stanford-corenlp-latest.zip && \
	rm stanford-corenlp-latest.zip

WORKDIR stanford-corenlp-4.0.0

RUN export CLASSPATH="`find . -name '*.jar'`"

ENV PORT 9000

EXPOSE $PORT

CMD java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000