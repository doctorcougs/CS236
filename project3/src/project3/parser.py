"""Parser for Datalog programs.

Provides the parser and error interface for when parsing fails for Datalog
programs.
"""

from typing import Iterator

from project3.datalogprogram import DatalogProgram, Parameter, Predicate, Rule
from project3.token import Token, TokenType


class UnexpectedTokenException(Exception):
    """Class for parsing errors.

    A parse error is when the actual token does not have the correct type
    according to the state of the parser. In other words, the parser is
    expecting a specific token type but the actual token at that point does
    not match the expected type.

    Attributes:
        expected_type (TokenType): The type that was expected in the parse.
        token (Token): The actual token that was encountered.
    """

    def __init__(
        self,
        expected_type: TokenType,
        token: Token,
        message: str = "A parse error occurred due to an unexpected token",
    ) -> None:
        super().__init__(message)
        self.expected_type = expected_type
        self.token = token


class TokenStream:
    """Class for managing the token iterator from the lexer.

    A `TokenStream` is a wrapper for the `Iterator[Token]` from the lexer that
    provides core functions for parsing -- `match` and `advance` -- along with an
    additional function for checking if the current token has a type that
    belongs to a set of types -- useful for checking FIRST and FOLLOW sets -- and
    a way to get tho value from the current token.

    Attributes:
        token_iterator (Iterator[Token]): A token iterator.
        token (Token): The current token.
    """

    def __init__(self, token_iterator: Iterator[Token]) -> None:
        self._token_iterator = token_iterator
        self.advance()

    def __repr__(self) -> str:
        return f"TokenStream(token={self.token!r}, _token_iterator={self._token_iterator!r})"

    def advance(self) -> None:
        """Advances the iterator and updates the token.

        The last token in the iterator is stuttered meaning that it is repeated
        on every subsequent call.

        **WARNING**: `advance` side-effects the `token` and `token_iterator`.
        This side-effect means that the previous token is gone and cannot be
        recovered. There is no deep-copy for a `TokenStream`, so it's a _use
        once_ object. That is fine for parsing.
        """
        try:
            self.token = next(self._token_iterator)
        except StopIteration:
            pass

    def match(self, expected_type: TokenType) -> None:
        """Return if token matches expected type.

        `match` returns iff the expected type matches the current taken. If
        ever the token type does not match the expected type, it raises an exception
        indicating a match failure. The exception includes the expected token
        type and the token that did not match.

        Args:
            expected_type (TokenType): The expected token type in the stream for a successful match.

        Raises:
            error (UnexpectedTokenException): Error if the type of the current token does not match.
        """
        if self.token.token_type != expected_type:
            raise UnexpectedTokenException(expected_type, self.token)

    def member_of(self, token_types: set[TokenType]) -> bool:
        """Returns true iff the current token type is in the specified type.

        `member_of` is a way to determine if the type of the current token is
        in a set of token types. It is especially useful for checking membership
        in FIRST and FOLLOW sets when implementing a table driven parser.
        The FIRST and FOLLOW sets are used to determine which alternative to use
        in a grammar rule with alternatives.

        Args:
            token_types: A set of token types.

        Returns:
            out: True iff the current token type is in the set of token types.
        """
        return self.token.token_type in token_types

    def value(self) -> str:
        """Return the value attribute of the current token."""
        return self.token.value


def scheme(token: TokenStream) -> Predicate:
    token.match("ID")
    name = token.value()
    token.advance()

    token.match("LEFT_PAREN")
    token.advance()

    token.match("ID")
    parameters = [Parameter(token.value(), parameter_type="ID")]
    token.advance()
    parameters.extend(id_list(token))

    token.match("RIGHT_PAREN")
    token.advance()

    return Predicate(name, parameters)


def scheme_list(token: TokenStream) -> list[Predicate]:
    if token.token.token_type == "ID":
        i = scheme(token)
        return [i] + scheme_list(token)
    return []


def fact(token: TokenStream) -> Predicate:
    token.match("ID")
    name = token.value()
    token.advance()

    token.match("LEFT_PAREN")
    token.advance()

    token.match("STRING")
    parameters = [Parameter(token.value(), parameter_type="STRING")]
    token.advance()
    parameters.extend(string_list(token))

    token.match("RIGHT_PAREN")
    token.advance()

    token.match("PERIOD")
    token.advance()

    return Predicate(name, parameters)


def fact_list(token: TokenStream) -> list[Predicate]:
    if token.token.token_type == "ID":
        i = fact(token)
        return [i] + fact_list(token)
    return []


def rule(token: TokenStream) -> Rule:
    head = head_predicate(token)

    token.match("COLON_DASH")
    token.advance()

    body = [predicate(token)]
    body.extend(predicate_list(token))

    token.match("PERIOD")
    token.advance()

    return Rule(head, body)


def rule_list(token: TokenStream) -> list[Rule]:
    rules = []
    if token.token.token_type == "ID":
        rules.append(rule(token))
        rules.extend(rule_list(token))
    return rules


def query(token: TokenStream) -> Predicate:
    pred = predicate(token)
    token.match("Q_MARK")
    token.advance()
    return pred


def query_list(token: TokenStream) -> list[Predicate]:
    queries = []
    if token.token.token_type == "ID":
        queries.append(query(token))
        queries.extend(query_list(token))
    return queries


def id_list(token: TokenStream) -> list[Parameter]:
    params = []
    while token.token.token_type == "COMMA":
        token.advance()
        token.match("ID")
        params.append(Parameter(token.value(), parameter_type="ID"))
        token.advance()
    return params


def string_list(token: TokenStream) -> list[Parameter]:
    params = []
    while token.token.token_type == "COMMA":
        token.advance()
        token.match("STRING")
        params.append(Parameter(token.value(), parameter_type="STRING"))
        token.advance()
    return params


def head_predicate(token: TokenStream) -> Predicate:
    token.match("ID")
    name = token.value()
    token.advance()

    token.match("LEFT_PAREN")
    token.advance()

    token.match("ID")
    params = [Parameter(token.value(), parameter_type="ID")]
    token.advance()
    params.extend(id_list(token))

    token.match("RIGHT_PAREN")
    token.advance()

    return Predicate(name, params)


def predicate(token: TokenStream) -> Predicate:
    token.match("ID")
    name = token.value()
    token.advance()

    token.match("LEFT_PAREN")
    token.advance()

    p = parameter(token)
    params = [p]
    params.extend(parameter_list(token))

    token.match("RIGHT_PAREN")
    token.advance()

    return Predicate(name, params)


def predicate_list(token: TokenStream) -> list[Predicate]:
    preds = []
    while token.token.token_type == "COMMA":
        token.advance()
        preds.append(predicate(token))
    return preds


def parameter(token: TokenStream) -> Parameter:
    if token.token.token_type == "STRING":
        p = Parameter(token.value(), parameter_type="STRING")
    elif token.token.token_type == "ID":
        p = Parameter(token.value(), parameter_type="ID")
    else:
        raise Exception(f"Unexpected token in parameter: {token.token}")
    token.advance()
    return p


def parameter_list(token: TokenStream) -> list[Parameter]:
    params = []
    while token.token.token_type == "COMMA":
        token.advance()
        params.append(parameter(token))
    return params


def datalog_program(token: TokenStream) -> DatalogProgram:
    """Top-level grammar rule for a Datalog program.

    The function directly matches its associated grammar rule by matching
    on keywords and collecting returns from other non-terminal rules to
    build an instance of a `DatalogProgram`.

    Pseudo-code:
    ```
    token.match('SCHEMES')
    token.advance()
    token.match('COLON')
    token.advance()

    schemes: list[Predicate] = [scheme(token)]
    schemes.extend(scheme_list(token))

    # Other matches, advances, and rules for the rest of a Datalog Program

    return DatalogProgram(schemes, facts, rules, queries)
    ```

    Args:
        token (TokenStream]): A token stream.

    Returns:
        program (DatalogProgram): The Datalog program from the parse.
    """

    token.match("SCHEMES")
    token.advance()
    token.match("COLON")
    token.advance()

    schemes = [scheme(token)]
    schemes.extend(scheme_list(token))

    token.match("FACTS")
    token.advance()
    token.match("COLON")
    token.advance()

    facts = fact_list(token)

    token.match("RULES")
    token.advance()
    token.match("COLON")
    token.advance()

    rules = rule_list(token)

    token.match("QUERIES")
    token.advance()
    token.match("COLON")
    token.advance()

    queries = [query(token)]
    queries.extend(query_list(token))

    token.match("EOF")

    return DatalogProgram(schemes, facts, rules, queries)


def parse(token_iterator: Iterator[Token]) -> DatalogProgram:
    """Parse a datalog program.

    A convenience function that avoids having to create an instance of the
    `TokenStream`

    Args:
        token_iterator (Iterator[Token]): A token iterator.

    Returns:

        program (DatalogProgram): The Datalog program from the parse.
    """
    token: TokenStream = TokenStream(token_iterator)
    return datalog_program(token)
