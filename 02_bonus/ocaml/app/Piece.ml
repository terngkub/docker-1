type t = Empty | O | X


let to_string (piece:t) =
  match piece with
  | Empty -> "-"
  | O     -> "O"
  | X     -> "X"
