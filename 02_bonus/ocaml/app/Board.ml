type t = Grid.t * Grid.t * Grid.t * Grid.t * Grid.t * Grid.t * Grid.t * Grid.t * Grid.t 


let init = (Grid.init, Grid.init, Grid.init, Grid.init, Grid.init, Grid.init, Grid.init, Grid.init, Grid.init)


let print (a, b, c, d, e, f, g, h, i) =
  let rec loop n =
    if n >= 9 then ()
    else begin
      let set = n / 3 in
      let line = n mod 3 in
      begin match set with
      | 0 -> print_endline ((Grid.to_string_line a line) ^ " | " ^ (Grid.to_string_line b line) ^ " | " ^(Grid.to_string_line c line))
      | 1 -> print_endline ((Grid.to_string_line d line) ^ " | " ^ (Grid.to_string_line e line) ^ " | " ^(Grid.to_string_line f line))
      | _ -> print_endline ((Grid.to_string_line g line) ^ " | " ^ (Grid.to_string_line h line) ^ " | " ^(Grid.to_string_line i line))
      end;
      if n = 2 || n = 5 then print_endline "---------------------";
      loop (n + 1)
    end
  in
  loop 0


let is_valid (a, b, c, d, e, f, g, h, i) grid_num piece_num =
  match grid_num with
  | 1 -> Grid.is_valid a piece_num
  | 2 -> Grid.is_valid b piece_num
  | 3 -> Grid.is_valid c piece_num
  | 4 -> Grid.is_valid d piece_num
  | 5 -> Grid.is_valid e piece_num
  | 6 -> Grid.is_valid f piece_num
  | 7 -> Grid.is_valid g piece_num
  | 8 -> Grid.is_valid h piece_num
  | 9 -> Grid.is_valid i piece_num
  | _ -> false


let fill board grid_num piece_num value player =
  match board with
  | (a, b, c, d, e, f, g, h, i) when grid_num = 1 -> (Grid.fill a grid_num piece_num value player, b, c, d, e, f, g, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 2 -> (a, Grid.fill b grid_num piece_num value player, c, d, e, f, g, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 3 -> (a, b, Grid.fill c grid_num piece_num value player, d, e, f, g, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 4 -> (a, b, c, Grid.fill d grid_num piece_num value player, e, f, g, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 5 -> (a, b, c, d, Grid.fill e grid_num piece_num value player, f, g, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 6 -> (a, b, c, d, e, Grid.fill f grid_num piece_num value player, g, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 7 -> (a, b, c, d, e, f, Grid.fill g grid_num piece_num value player, h, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 8 -> (a, b, c, d, e, f, g, Grid.fill h grid_num piece_num value player, i)
  | (a, b, c, d, e, f, g, h, i) when grid_num = 9 -> (a, b, c, d, e, f, g, h, Grid.fill i grid_num piece_num value player)
  | _ -> board


let check (a, b, c, d, e, f, g, h, i) value =
  if      a = value && b = value && c = value then true
  else if d = value && e = value && f = value then true
  else if g = value && h = value && i = value then true
  else if a = value && d = value && g = value then true
  else if b = value && e = value && h = value then true
  else if c = value && f = value && i = value then true
  else if a = value && e = value && i = value then true
  else if c = value && e = value && g = value then true
  else false
