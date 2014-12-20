// Learn more about F# at http://fsharp.net
// See the 'F# Tutorial' project for more help.

//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
//Find the sum of all the multiples of 3 or 5 below 1000.


let sumMultOfXBelowY (x : int) (y : int) = seq {for i in 1 .. (y-1)/x -> x * i}
                                           |> Seq.sum

let sumOf3Or5BelowY (y : int) = List.sum [ sumMultOfXBelowY 3 y; sumMultOfXBelowY 5 y; -(sumMultOfXBelowY 15 y) ]

[<EntryPoint>]
let main argv =
    try
        printfn "%O" (sumOf3Or5BelowY (argv.[0] |> int))
    with
        | _ -> ()
    0 // return an integer exit code