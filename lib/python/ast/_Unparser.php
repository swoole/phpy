<?php
namespace python\ast;

/**
* @property $buffer
*/
class _Unparser
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Unparser();
    }

    public function block()
    {
        return $this->_self->block();
    }

    public function buffer_writer($text)
    {
        return $this->_self->buffer_writer($text);
    }

    public function delimit()
    {
        return $this->_self->delimit();
    }

    public function delimit_if($start, $end, $condition)
    {
        return $this->_self->delimit_if($start, $end, $condition);
    }

    public function fill($text = "")
    {
        return $this->_self->fill($text);
    }

    public function generic_visit($node)
    {
        return $this->_self->generic_visit($node);
    }

    public function get_precedence($node)
    {
        return $this->_self->get_precedence($node);
    }

    public function get_raw_docstring($node)
    {
        return $this->_self->get_raw_docstring($node);
    }

    public function get_type_comment($node)
    {
        return $this->_self->get_type_comment($node);
    }

    public function interleave($inter, $f, $seq)
    {
        return $this->_self->interleave($inter, $f, $seq);
    }

    public function items_view($traverser, $items)
    {
        return $this->_self->items_view($traverser, $items);
    }

    public function maybe_newline()
    {
        return $this->_self->maybe_newline();
    }

    public function require_parens($precedence, $node)
    {
        return $this->_self->require_parens($precedence, $node);
    }

    public function set_precedence($precedence)
    {
        return $this->_self->set_precedence($precedence);
    }

    public function traverse($node)
    {
        return $this->_self->traverse($node);
    }

    public function visit($node)
    {
        return $this->_self->visit($node);
    }

    public function visit_AnnAssign($node)
    {
        return $this->_self->visit_AnnAssign($node);
    }

    public function visit_Assert($node)
    {
        return $this->_self->visit_Assert($node);
    }

    public function visit_Assign($node)
    {
        return $this->_self->visit_Assign($node);
    }

    public function visit_AsyncFor($node)
    {
        return $this->_self->visit_AsyncFor($node);
    }

    public function visit_AsyncFunctionDef($node)
    {
        return $this->_self->visit_AsyncFunctionDef($node);
    }

    public function visit_AsyncWith($node)
    {
        return $this->_self->visit_AsyncWith($node);
    }

    public function visit_Attribute($node)
    {
        return $this->_self->visit_Attribute($node);
    }

    public function visit_AugAssign($node)
    {
        return $this->_self->visit_AugAssign($node);
    }

    public function visit_Await($node)
    {
        return $this->_self->visit_Await($node);
    }

    public function visit_BinOp($node)
    {
        return $this->_self->visit_BinOp($node);
    }

    public function visit_BoolOp($node)
    {
        return $this->_self->visit_BoolOp($node);
    }

    public function visit_Break($node)
    {
        return $this->_self->visit_Break($node);
    }

    public function visit_Call($node)
    {
        return $this->_self->visit_Call($node);
    }

    public function visit_ClassDef($node)
    {
        return $this->_self->visit_ClassDef($node);
    }

    public function visit_Compare($node)
    {
        return $this->_self->visit_Compare($node);
    }

    public function visit_Constant($node)
    {
        return $this->_self->visit_Constant($node);
    }

    public function visit_Continue($node)
    {
        return $this->_self->visit_Continue($node);
    }

    public function visit_Delete($node)
    {
        return $this->_self->visit_Delete($node);
    }

    public function visit_Dict($node)
    {
        return $this->_self->visit_Dict($node);
    }

    public function visit_DictComp($node)
    {
        return $this->_self->visit_DictComp($node);
    }

    public function visit_Ellipsis($node)
    {
        return $this->_self->visit_Ellipsis($node);
    }

    public function visit_ExceptHandler($node)
    {
        return $this->_self->visit_ExceptHandler($node);
    }

    public function visit_Expr($node)
    {
        return $this->_self->visit_Expr($node);
    }

    public function visit_For($node)
    {
        return $this->_self->visit_For($node);
    }

    public function visit_FormattedValue($node)
    {
        return $this->_self->visit_FormattedValue($node);
    }

    public function visit_FunctionDef($node)
    {
        return $this->_self->visit_FunctionDef($node);
    }

    public function visit_FunctionType($node)
    {
        return $this->_self->visit_FunctionType($node);
    }

    public function visit_GeneratorExp($node)
    {
        return $this->_self->visit_GeneratorExp($node);
    }

    public function visit_Global($node)
    {
        return $this->_self->visit_Global($node);
    }

    public function visit_If($node)
    {
        return $this->_self->visit_If($node);
    }

    public function visit_IfExp($node)
    {
        return $this->_self->visit_IfExp($node);
    }

    public function visit_Import($node)
    {
        return $this->_self->visit_Import($node);
    }

    public function visit_ImportFrom($node)
    {
        return $this->_self->visit_ImportFrom($node);
    }

    public function visit_JoinedStr($node)
    {
        return $this->_self->visit_JoinedStr($node);
    }

    public function visit_Lambda($node)
    {
        return $this->_self->visit_Lambda($node);
    }

    public function visit_List($node)
    {
        return $this->_self->visit_List($node);
    }

    public function visit_ListComp($node)
    {
        return $this->_self->visit_ListComp($node);
    }

    public function visit_Match($node)
    {
        return $this->_self->visit_Match($node);
    }

    public function visit_MatchAs($node)
    {
        return $this->_self->visit_MatchAs($node);
    }

    public function visit_MatchClass($node)
    {
        return $this->_self->visit_MatchClass($node);
    }

    public function visit_MatchMapping($node)
    {
        return $this->_self->visit_MatchMapping($node);
    }

    public function visit_MatchOr($node)
    {
        return $this->_self->visit_MatchOr($node);
    }

    public function visit_MatchSequence($node)
    {
        return $this->_self->visit_MatchSequence($node);
    }

    public function visit_MatchSingleton($node)
    {
        return $this->_self->visit_MatchSingleton($node);
    }

    public function visit_MatchStar($node)
    {
        return $this->_self->visit_MatchStar($node);
    }

    public function visit_MatchValue($node)
    {
        return $this->_self->visit_MatchValue($node);
    }

    public function visit_Module($node)
    {
        return $this->_self->visit_Module($node);
    }

    public function visit_Name($node)
    {
        return $this->_self->visit_Name($node);
    }

    public function visit_NamedExpr($node)
    {
        return $this->_self->visit_NamedExpr($node);
    }

    public function visit_Nonlocal($node)
    {
        return $this->_self->visit_Nonlocal($node);
    }

    public function visit_Pass($node)
    {
        return $this->_self->visit_Pass($node);
    }

    public function visit_Raise($node)
    {
        return $this->_self->visit_Raise($node);
    }

    public function visit_Return($node)
    {
        return $this->_self->visit_Return($node);
    }

    public function visit_Set($node)
    {
        return $this->_self->visit_Set($node);
    }

    public function visit_SetComp($node)
    {
        return $this->_self->visit_SetComp($node);
    }

    public function visit_Slice($node)
    {
        return $this->_self->visit_Slice($node);
    }

    public function visit_Starred($node)
    {
        return $this->_self->visit_Starred($node);
    }

    public function visit_Subscript($node)
    {
        return $this->_self->visit_Subscript($node);
    }

    public function visit_Try($node)
    {
        return $this->_self->visit_Try($node);
    }

    public function visit_Tuple($node)
    {
        return $this->_self->visit_Tuple($node);
    }

    public function visit_UnaryOp($node)
    {
        return $this->_self->visit_UnaryOp($node);
    }

    public function visit_While($node)
    {
        return $this->_self->visit_While($node);
    }

    public function visit_With($node)
    {
        return $this->_self->visit_With($node);
    }

    public function visit_Yield($node)
    {
        return $this->_self->visit_Yield($node);
    }

    public function visit_YieldFrom($node)
    {
        return $this->_self->visit_YieldFrom($node);
    }

    public function visit_alias($node)
    {
        return $this->_self->visit_alias($node);
    }

    public function visit_arg($node)
    {
        return $this->_self->visit_arg($node);
    }

    public function visit_arguments($node)
    {
        return $this->_self->visit_arguments($node);
    }

    public function visit_comprehension($node)
    {
        return $this->_self->visit_comprehension($node);
    }

    public function visit_keyword($node)
    {
        return $this->_self->visit_keyword($node);
    }

    public function visit_match_case($node)
    {
        return $this->_self->visit_match_case($node);
    }

    public function visit_withitem($node)
    {
        return $this->_self->visit_withitem($node);
    }

    public function write($text)
    {
        return $this->_self->write($text);
    }

}
